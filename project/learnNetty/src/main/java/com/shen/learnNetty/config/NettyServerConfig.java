package com.shen.learnNetty.config;


import com.shen.learnNetty.handle.SimpleInboundHandler;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class NettyServerConfig {

    private static final Logger logger = LoggerFactory.getLogger(NettyServerConfig.class);

    @Value("${netty.port}")
    private int port;

    @Bean(destroyMethod = "shutdownGracefully")
    public EventLoopGroup bossGroup() {
        return new NioEventLoopGroup();
    }

    @Bean(destroyMethod = "shutdownGracefully")
    public EventLoopGroup workerGroup() {
        return new NioEventLoopGroup();
    }

    @Bean
    public ServerBootstrap bootstrap(EventLoopGroup bossGroup, EventLoopGroup workerGroup) {
        ServerBootstrap b = new ServerBootstrap();
        b.group(bossGroup, workerGroup)
                .channel(NioServerSocketChannel.class)
                .childHandler(new ChannelInitializer<SocketChannel>() {
                    @Override
                    protected void initChannel(SocketChannel ch) throws Exception {
                        // 在这里添加你的处理器
                        ch.pipeline().addLast(new SimpleInboundHandler());
                    }
                });
        return b;
    }

    @Bean
    public ChannelFuture start(ServerBootstrap bootstrap) throws InterruptedException {
        ChannelFuture future = bootstrap.bind(port).sync();
        if (future.isSuccess()) {
            logger.info("Started server at port: {}", port);
        } else {
            logger.error("Failed to start server!");
            future.cause().printStackTrace();
        }
        return future;
    }
}
