package br.com.alura.rh.services;

import br.com.alura.rh.model.Employee;

import java.math.BigDecimal;

public interface SalaryRaiseValidation {
    void validate(Employee employee, BigDecimal salaryRaise);
}
