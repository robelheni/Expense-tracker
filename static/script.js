// API Base URL
const API_URL = 'http://127.0.0.1:8000';

// Load expenses when page loads
window.addEventListener('DOMContentLoaded', loadExpenses);

// Handle form submission
document.getElementById('expenseForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Get form values
    const description = document.getElementById('description').value;
    const amount = parseFloat(document.getElementById('amount').value);
    
    // Send to API
    await fetch(`${API_URL}/expenses`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ description, amount })
    });
    
    // Clear form
    document.getElementById('expenseForm').reset();
    
    // Reload expenses
    loadExpenses();
});

// Load and display expenses
async function loadExpenses() {
    // Fetch expenses from API
    const response = await fetch(`${API_URL}/expenses`);
    const data = await response.json();
    const expenses = data.expenses;
    
    // Update total
    const total = expenses.reduce((sum, exp) => sum + exp.amount, 0);
    document.getElementById('totalAmount').textContent = `$${total.toFixed(2)}`;
    
    // Display expenses
    const listDiv = document.getElementById('expensesList');
    
    if (expenses.length === 0) {
        listDiv.innerHTML = '<p class="empty-state">No expenses yet. Add one above!</p>';
        return;
    }
    
    listDiv.innerHTML = expenses.map(expense => `
        <div class="expense-item">
            <div class="expense-info">
                <div class="expense-description">${expense.description}</div>
            </div>
            <span class="expense-amount">$${expense.amount.toFixed(2)}</span>
            <button class="delete-btn" onclick="deleteExpense(${expense.id})">Delete</button>
        </div>
    `).join('');
}

// Delete an expense
async function deleteExpense(id) {
    if (!confirm('Are you sure you want to delete this expense?')) return;
    
    await fetch(`${API_URL}/expenses/${id}`, { method: 'DELETE' });
    loadExpenses();
}