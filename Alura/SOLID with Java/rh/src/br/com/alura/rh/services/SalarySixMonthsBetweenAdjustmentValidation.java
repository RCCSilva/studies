package br.com.alura.rh.services;

import br.com.alura.rh.ValidationException;
import br.com.alura.rh.model.Employee;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class SalarySixMonthsBetweenAdjustmentValidation implements SalaryRaiseValidation {

    @Override
    public void validate(Employee employee, BigDecimal salaryRaise) {
        long months = ChronoUnit.MONTHS.between(employee.getDateLastReadjustment(), LocalDate.now());

        if (months < 6) {
            throw new ValidationException("Salary adjustment may only be applied 6 months after the last one");
        }
    }
}
