using System.Collections.Generic;
using Domain.Entities;

namespace Application.Interfaces
{
    public interface ICustomerRepository
    {
        void Add(Customer customer);
        IEnumerable<Customer> GetAll();
    }
}
