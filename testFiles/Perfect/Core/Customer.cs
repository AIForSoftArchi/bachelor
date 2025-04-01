namespace OnionArchitecture.Domain
    public class Customer
    {
        public int Id { get; private set; }
        public string Name { get; private set; }
        public string Email { get; private set; }

        private Customer() { }

        public static Customer Create(string name, string email)
        {
            return new Customer { Name = name, Email = email };
        }
    }