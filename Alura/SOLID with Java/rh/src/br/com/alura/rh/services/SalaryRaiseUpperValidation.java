package br.com.alura.rh.services;

import br.com.alura.rh.ValidationException;
import br.com.alura.rh.model.Employee;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class SalaryRaiseUpperValidation implements SalaryRaiseValidation {

    @Override
    public void validate(Employee employee, BigDecimal salaryRaise) {
        BigDecimal percentageAdjustment = salaryRaise.divide(employee.getSalary(), RoundingMode.HALF_UP);

        if (percentageAdjustment.compareTo(new BigDecimal("0.4")) > 0) {
            throw new ValidationException("Salary adjustment must not be greater than 40%");
        }
    }
}
