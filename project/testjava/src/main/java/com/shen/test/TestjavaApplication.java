package com.shen.test;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan(basePackages = {"com.shen.test.**"})
public class TestjavaApplication {

	public static void main(String[] args) {
		SpringApplication.run(TestjavaApplication.class, args);
	}

}
