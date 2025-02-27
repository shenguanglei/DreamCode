1. **消息推送概述**：消息推送是运营人员向用户网页或移动设备 APP 主动推送消息，分为 Web 端和移动端。文中需求是事件触发时，Web 页面通知小红点实时 + 1，涉及服务端消息推送表和前端获取未读消息数的操作123。
2. 消息推送常见方案
   - **短轮询**：浏览器按指定时间间隔向服务器发 HTTP 请求获取未读消息，用 JS 定时器可实现。优点是简单，缺点是会造成服务端压力大，浪费资源。
   - **长轮询**：服务端数据不变时 hold 住请求，变了或超时才返回，客户端再立即发起下一次请求。使用 Apollo 配置中心的 DeferredResult 实现，能减少资源浪费，但仍会产生较多请求6。
   - **iframe 流**：在页面插入隐藏<iframe>标签，通过 src 请求消息数量 API 接口创建长连接，服务端向其传输数据。实现简单，但服务器开销大，浏览器会一直 loading，不推荐使用。
   - **SSE（服务器发送事件）**：服务端到客户端的单向消息推送，基于 HTTP 协议。与 WebSocket 相比，它实现简单、开发成本低、支持断线重连，但只能单向通信且仅支持文本消息。适用于站内信等场景。
   - **WebSocket**：基于 TCP 连接的全双工通信协议，需一次握手创建持久连接。Spring Boot 整合时需引入相关包，开发成本较高，但性能高、开销小，适用于游戏、即时通信等双向实时更新场景。
   - **MQTT**：基于发布 / 订阅模式的轻量级通讯协议，构建于 TCP/IP 协议上，适用于物联网场景。它能在不可靠网络环境为设备提供可靠消息服务，但实现相对复杂。
3. **方案对比总结**：每种方案都有其特点和适用场景。短轮询简单但资源浪费严重；长轮询有所优化但仍有不足；iframe 流体验差；SSE 单向推送适合特定场景；WebSocket 全双工通信性能好但开发复杂；MQTT 轻量级且适用于物联网，开发也较复杂202122