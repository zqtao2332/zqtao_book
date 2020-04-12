# MySQL总结之查询缓存

通过`show variables like '%query_cache%'`查看默认的数据库配置

![数据库默认配置](https://upload-images.jianshu.io/upload_images/18375227-42c0d6317f9323e9.png?imageMogr2/auto-orient/strip|imageView2/2/w/391/format/webp)

## 1.1缓存相关配置概念

**have_query_cache**：当前的MySQL版本是否支持“查询缓存功能”

**query_cache_limit**：MySQL能够缓存的最大查询结果，查询结果大于该值时不会被缓存。

