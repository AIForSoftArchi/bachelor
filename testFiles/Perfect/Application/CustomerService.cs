namespace OnionArchitecture.Application
{
    using OnionArchitecture.Domain;
    
    public interface ICustomerService
    {
        CustomerDto GetCustomer(int id);
        void CreateCustomer(string name, string email);
    }
    
    public class CustomerService : ICustomerService
    {
        private readonly ICustomerRepository _customerRepository;
        
        public CustomerService(ICustomerRepository customerRepository)
        {
            _customerRepository = customerRepository;
        }

        public CustomerDto GetCustomer(int id)
        {
            var customer = _customerRepository.GetCustomerById(id);
            return customer == null ? null : new CustomerDto(customer.Id, customer.Name, customer.Email);
        }

        public void CreateCustomer(string name, string email)
        {
            var customer = Customer.Create(name, email);
            _customerRepository.AddCustomer(customer);
        }
    }

    public record CustomerDto(int Id, string Name, string Email);
}