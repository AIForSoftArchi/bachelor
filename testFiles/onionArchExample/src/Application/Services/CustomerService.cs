using System.Collections.Generic;
using Application.Interfaces;
using Domain.Entities;
using Application.Models;

namespace Application.Services
{
    public class CustomerService : ICustomerService
    {
        private readonly ICustomerRepository _repository;

        public CustomerService(ICustomerRepository repository)
        {
            _repository = repository;
        }

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
