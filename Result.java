package com.example.demo.common;

import java.math.BigDecimal;
import java.util.Date;

import com.example.demo.systempara.entity.Systempara;

import lombok.Data;
import lombok.experimental.Accessors;
/*AJAX请求*/
@Data
@Accessors(chain = true)
public class Result {
	private static final long serialVersionUID = 1L;

	private boolean sucess = true;
	private String msg;
	private Object data;
}
