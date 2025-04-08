using System.Collections.Generic;
using Application.Models;

namespace Application.Interfaces
{
    public interface ICustomerService
    {
        void AddCustomer(CreateCustomerRequest request);
        IEnumerable<CustomerDTO> GetCustomers();
    }
}
