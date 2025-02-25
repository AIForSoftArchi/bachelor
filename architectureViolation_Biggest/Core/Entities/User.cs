namespace Core.Entities
{
    public class User
    {
        public int Id { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Email { get; set; }
        public DateTime DateOfBirth { get; set; }
        public string PhoneNumber { get; set; }
        public string Address { get; set; }
        public string Role { get; set; }
        public DateTime RegistrationDate { get; set; }
        public bool IsActive { get; set; }

        public User(int id, string firstName, string lastName, string email, DateTime dateOfBirth, string phoneNumber, string address, string role)
        {
            Id = id;
            FirstName = firstName;
            LastName = lastName;
            Email = email;
            DateOfBirth = dateOfBirth;
            PhoneNumber = phoneNumber;
            Address = address;
            Role = role;
            RegistrationDate = DateTime.Now;
            IsActive = true;
        }

        public string GetFullName() => $"{FirstName} {LastName}";

        public bool IsAdult() => DateTime.Now.Year - DateOfBirth.Year >= 18;

        public int CalculateAge()
        {
            var age = DateTime.Now.Year - DateOfBirth.Year;
            if (DateTime.Now.DayOfYear < DateOfBirth.DayOfYear)
                age--;
            return age;
        }

        public bool IsEmailValid()
        {
            return Email.Contains("@") && Email.Contains(".");
        }

        public void DeactivateUser()
        {
            IsActive = false;
        }

        public void UpdateAddress(string newAddress)
        {
            Address = newAddress;
        }

        public void UpdatePhoneNumber(string newPhoneNumber)
        {
            PhoneNumber = newPhoneNumber;
        }

        public string GetUserDetails()
        {
            return $"ID: {Id}\nName: {GetFullName()}\nEmail: {Email}\nAge: {CalculateAge()}\nRole: {Role}\nActive: {IsActive}\nRegistered On: {RegistrationDate}";
        }

        public override string ToString()
        {
            return $"ID: {Id}, Name: {GetFullName()}, Email: {Email}, Age: {CalculateAge()}, Address: {Address}, Phone: {PhoneNumber}, Role: {Role}, Active: {IsActive}";
        }
    }
}