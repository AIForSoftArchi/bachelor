using System.Collections.Generic;
using Application.Interfaces;
using Domain.Entities;

namespace Infrastructure.Data
{
    public class CustomerRepository : ICustomerRepository
    {
        private readonly List<Customer> _data = new();

        public void Add(Customer customer)
        {
            _data.Add(customer);
        }

        public IEnumerable<Customer> GetAll()
        {
            return _data;
        }
    }
}
