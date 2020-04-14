# MySQL总结之查询缓存

通过`show variables like '%query_cache%'`查看默认的数据库配置

![数据库默认配置](https://upload-images.jianshu.io/upload_images/18375227-42c0d6317f9323e9.png?imageMogr2/auto-orient/strip|imageView2/2/w/391/format/webp)

## 1.1缓存相关配置概念

**have_query_cache**：当前的MySQL版本是否支持“查询缓存功能”

**query_cache_limit**：MySQL能够缓存的最大查询结果，查询结果大于该值时不会被缓存。

**query_cache_min_res_unit**: 查询缓存分配的最小块（字节）。默认值是4096（4KB）。当查询进行时，MySQL把查询结果保存在query cache，但是如果保存的结果比较大，超过了query_cache_min_res_unit的值，这时候MySQL将一边检索结果，一边进行保存结果。他保存结果也是按默认大小先分配一块空间，如果不够，又要申请新的空间给他。如果查询结果比较小，默认的query_cache_min_res_unit可能造成大量的内存碎片，如果查询结果比较大，默认的query_cache_min_res_unit又不够，导致一直分配块空间，所以可以根据实际需求，调节query_cache_min_res_unit的大小。

**query_cache_size:**为缓存查询结果分配的总内存。

**query_cache_type**:默认为on，可以缓存除了以select sql_no_cache开头的所有查询结果。

**query_cache_wlock_invalidate**:如果该表被锁住，是否返回缓存中的数据，默认是关闭的。

## **1.2查询缓存原理**

MySQL的查询缓存的实质就是缓存SQL的hash值和SQL的查询结果，如果是执行相同的SQL，那么MySQL服务器则会直接返回缓存中的结果集，而不再进行后续的解析，优化，寻找最低成本的执行计划等一系列操作，大大提升了查询速度。

上述是查询缓存的优点，但是查询缓存也有两个弊端

**第一个弊端是如果表中的数据有一条发生了变化，那么缓存好的结果将不再有效。对于频繁更新的表，查询缓存将不再适用。**

```
比如一张表里面只有两个字段，分别是id和name，数据有一条为1，张三。我使用select * from 表名 where name=“张三”来进行查询，MySQL发现查询缓存中没有此数据，会进行一系列的解析，优化等操作进行数据的查询，查询结束之后将该SQL的hash和查询结果缓存起来，并将查询结果返回给客户端。但是这个时候我有新增了一条数据2，张三。如果我还用相同的SQL来执行，他会根据该SQL的hash值去查询缓存中，那么结果就错了。所以MySQL对于数据有变化的表来说，会直接清空关于该表的所有缓存。这样其实是效率是很差的。
```

 **第二个弊端就是缓存机制是通过对SQL的hash，得出的值为key，查询结果为value来存放的，那么就意味着SQL必须完完全全一模一样，否则就命不中缓存。** 

```
我们都知道hash值的规则，就算很小的查询，哈希出来的结果差距是很多的，所以select * from 表名 where name=“张三”和SELECT * FROM 表名 WHERE NAME=“张三”和select * from 表名 where name = “张三”，三个SQL哈希出来的值是不一样的，大小写和空格影响了他们，所以并不能命中缓存，但其实他们搜索结果是完全一样的。
```

