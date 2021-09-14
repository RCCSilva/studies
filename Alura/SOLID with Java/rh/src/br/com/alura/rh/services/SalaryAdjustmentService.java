package br.com.alura.rh.services;

import br.com.alura.rh.model.Employee;
import org.jetbrains.annotations.NotNull;

import java.math.BigDecimal;
import java.util.List;

public class SalaryAdjustmentService {
    private final List<SalaryRaiseValidation> validations;

    SalaryAdjustmentService(List<SalaryRaiseValidation> validations) {
        this.validations = validations;
    }

    public void adjustEmployeeSalary(@NotNull Employee employee, BigDecimal salaryRaise) {
        validations.forEach(v -> v.validate(employee, salaryRaise));

        employee.setSalary(employee.getSalary().add(salaryRaise));
    }
}
