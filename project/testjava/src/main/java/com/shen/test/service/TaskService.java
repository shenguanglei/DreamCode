package com.shen.test.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
@Service
public class TaskService {
    private final ThreadPoolTaskExecutor taskExecutor;
    @Autowired
    public TaskService(@Qualifier("customThreadPool") ThreadPoolTaskExecutor taskExecutor) {
        this.taskExecutor = taskExecutor;
    }

    public void executeAsyncTask(int taskId) {
        taskExecutor.execute(() -> {
            System.out.println("Executing Task ID: " + taskId + " by Thread: " + Thread.currentThread().getName());
            try {
                Thread.sleep(2000); // 模拟耗时操作
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("Completed Task ID: " + taskId + " by Thread: " + Thread.currentThread().getName());
        });
    }

}
