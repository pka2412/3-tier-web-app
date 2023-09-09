document.addEventListener("DOMContentLoaded", () => {
  const expenseTable = document.getElementById("expenseTable");
  const incomeTable = document.getElementById("incomeTable");
  const expenseName = document.getElementById("expenseName");
  const expenseAmount = document.getElementById("expenseAmount");
  const addExpenseBtn = document.getElementById("addExpenseBtn");
  const incomeName = document.getElementById("incomeName");
  const incomeAmount = document.getElementById("incomeAmount");
  const addIncomeBtn = document.getElementById("addIncomeBtn");

  addExpenseBtn.addEventListener("click", () => {
    const name = expenseName.value;
    const amount = expenseAmount.value;
    if (name && amount) {
      fetch("/api/expenses", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ expenseName: name, expenseAmount: amount })
      })
      .then(() => {
        location.reload();
      });
    }
  });

  addIncomeBtn.addEventListener("click", () => {
    const name = incomeName.value;
    const amount = incomeAmount.value;
    if (name && amount) {
      fetch("/api/incomes", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ incomeName: name, incomeAmount: amount })
      })
      .then(() => {
        location.reload();
      });
    }
  });

  fetch("/api/expenses")
    .then(response => response.json())
    .then(expenses => {
      expenses.forEach(expense => {
        const row = expenseTable.insertRow();
        row.innerHTML = `<td>${expense.name}</td><td>$${expense.amount}</td>`;
      });
    });

  fetch("/api/incomes")
    .then(response => response.json())
    .then(incomes => {
      incomes.forEach(income => {
        const row = incomeTable.insertRow();
        row.innerHTML = `<td>${income.name}</td><td>$${income.amount}</td>`;
      });
    });
});
