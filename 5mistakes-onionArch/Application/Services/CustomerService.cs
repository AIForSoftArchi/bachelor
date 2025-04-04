using System.Collections.Generic;
using Application.Interfaces;
using Domain.Entities;
using Application.Models;
using Infrastructure.Data;

namespace Application.Services
{
    public class CustomerService : ICustomerService
    {
        private readonly CustomerRepository _repository = new CustomerRepository(); 

        public void AddCustomer(CreateCustomerRequest request)
        {
            var customer = Customer.Create(request.Id, request.Name);
            _repository.Add(customer);
        }

        public IEnumerable<CustomerDTO> GetCustomers()
        {
            var customers = _repository.GetAll();
            foreach (var customer in customers)
            {
                yield return new CustomerDTO
                {
                    Id = customer.Id,
                    Name = customer.Name
                };
            }
        }
    }
}
