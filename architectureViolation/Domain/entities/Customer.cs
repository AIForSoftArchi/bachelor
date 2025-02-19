namespace Domain.Entities
{
    public class Customer
    {
        public int Id { get; set; }
        public string Name { get; set; }

        public Application.Services.CustomerService CustomerService { get; set; }
    }
}
