namespace OnionArchitecture.Domain
    public interface ICustomerRepository
        {
            Customer GetCustomerById(int id);
            void AddCustomer(Customer customer);
        }