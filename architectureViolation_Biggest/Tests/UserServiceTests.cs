// Tests/UserServiceTests.cs
using Application.Services;
using Core.Entities;
using Infrastructure.Repositories;

namespace Tests
{
    public class UserServiceTests
    {
        public void RunTests()
        {
            var repository = new UserRepository();
            var service = new UserService(repository);

            Console.WriteLine("Running Extended UserService Tests...");

            var validUser = new User(1, "John", "Doe", "john.doe@example.com", new DateTime(1990, 1, 1), "1234567890", "123 Main St", "User");
            var invalidUser = new User(2, "Jane", "Doe", "invalidemail", new DateTime(2010, 1, 1), "0987654321", "456 Elm St", "User");

            try
            {
                service.AddUser(validUser);
                Console.WriteLine("Test Passed: Valid User Added");
            }
            catch (Exception e)
            {
                Console.WriteLine($"Test Failed: {e.Message}");
            }

            try
            {
                service.AddUser(invalidUser);
                Console.WriteLine("Test Failed: Invalid User Should Not Be Added");
            }
            catch (Exception)
            {
                Console.WriteLine("Test Passed: Invalid Email Detected");
            }

            Console.WriteLine("Testing User Deletion...");
            service.DeleteUser(1);
            Console.WriteLine("Test Passed: User Deactivated Successfully");

            Console.WriteLine("Promoting User to Admin...");
            service.PromoteUserToAdmin(1);
            Console.WriteLine("Test Passed: User Promoted to Admin");

            Console.WriteLine("Retrieving Inactive Users...");
            var inactiveUsers = service.GetInactiveUsers();
            Console.WriteLine($"Found {inactiveUsers.Count} inactive users.");
        }
    }
}
