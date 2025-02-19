using System.Collections.Generic;
using Application.Interfaces;

namespace Application.Services
{
    public class CustomerService : ICustomerService
    {
        private readonly List<string> _customers = new();

        public void AddCustomer(string name)
        {
            _customers.Add(name);
        }

        public List<string> GetCustomers() => _customers;
    }
}
