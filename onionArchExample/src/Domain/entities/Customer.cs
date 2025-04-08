namespace Domain.Entities
{
    public class Customer
    {
        public int Id { get; private set; }
        public string Name { get; private set; }

        private Customer() { } // For EF/Core or serialization

        private Customer(int id, string name)
        {
            Id = id;
            Name = name;
        }

        public static Customer Create(int id, string name)
        {
            // Add any domain validation here
            return new Customer(id, name);
        }
    }
}
