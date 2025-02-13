package com.shen.test.controller;




import com.shen.test.service.TaskService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TaskController {

    private final TaskService taskService;

    @Autowired
    public TaskController(TaskService taskService) {
        this.taskService = taskService;
    }

    @GetMapping("/submit-task")
    public String submitTask(@RequestParam int taskId) {
        taskService.executeAsyncTask(taskId);
        return "Task submitted with ID: " + taskId;
    }
}