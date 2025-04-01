namespace OnionArchitecture.Infrastructure
{
    using System.Collections.Generic;
    using OnionArchitecture.Domain;

    public class CustomerRepository : ICustomerRepository
    {
        private readonly List<Customer> _customers = new();
        
        public Customer GetCustomerById(int id)
        {
            return _customers.Find(c => c.Id == id);
        }

        public void AddCustomer(Customer customer)
        {
            customer.GetType().GetProperty("Id").SetValue(customer, _customers.Count + 1);
            _customers.Add(customer);
        }
    }
}