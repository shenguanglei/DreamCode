package com.shen.test.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;


import java.util.concurrent.ThreadFactory;
import java.util.concurrent.ThreadPoolExecutor;


@Configuration
public class ThreadPoolConfig {

    @Bean(name = "customThreadPool")
    public ThreadPoolTaskExecutor customThreadPool() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        // 1. 配置核心线程数
        executor.setCorePoolSize(5);
        // 2. 配置最大线程数
        executor.setMaxPoolSize(10);
        // 3. 配置线程空闲时间
        executor.setKeepAliveSeconds(60); // 60 秒
        // 4. 配置任务队列
        executor.setQueueCapacity(25);
        // 使用 ArrayBlockingQueue 作为任务队列
        executor.setTaskDecorator(runnable -> runnable);
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
        // 5. 配置线程工厂
        ThreadFactory threadFactory = new CustomThreadFactory("CustomThreadPool-");
        executor.setThreadFactory(threadFactory);
        // 6. 配置拒绝策略
        // 1. CallerRunsPolicy
        // 当触发拒绝策略时，由提交任务的线程来执行该任务。这样可以减缓新任务提交的速度，给线程池中的任务一些时间来完成。
        // 2. AbortPolicy
        // 这是默认的拒绝策略，当触发拒绝策略时，会直接抛出 RejectedExecutionException 异常，阻止系统正常运行。
        // 3. DiscardPolicy
        // 当触发拒绝策略时，会直接丢弃新提交的任务，不会抛出任何异常。
        // 4. DiscardOldestPolicy
        // 当触发拒绝策略时，会丢弃任务队列中最旧的任务，然后尝试重新提交新任务。
        // 2. AbortPolicy
        // executor.setRejectedExecutionHandler(new ThreadPoolExecutor.AbortPolicy());
        // 3. DiscardPolicy
        // executor.setRejectedExecutionHandler(new ThreadPoolExecutor.DiscardPolicy());
        // 4. DiscardOldestPolicy
        // executor.setRejectedExecutionHandler(new ThreadPoolExecutor.DiscardOldestPolicy());
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());

        // 7. 初始化线程池
        executor.initialize();
        return executor;
    }
}

