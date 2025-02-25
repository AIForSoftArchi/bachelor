using Application.Services;
using Core.Entities;

namespace Web.Controllers
{
    public class UserController
    {
        private readonly UserService _service;

        public UserController(UserService service)
        {
            _service = service;
        }

        public void CreateUser(int id, string firstName, string lastName, string email, DateTime dateOfBirth, string phoneNumber, string address, string role)
        {
            var user = new User(id, firstName, lastName, email, dateOfBirth, phoneNumber, address, role);
            _service.AddUser(user);
        }

        public void DisplayAllUsers()
        {
            var users = _service.GetAllUsers();
            foreach (var user in users)
            {
                Console.WriteLine(user.GetUserDetails());
            }
        }

        public void DeleteUserById(int id)
        {
            _service.DeleteUser(id);
            Console.WriteLine($"User with ID {id} has been deactivated.");
        }

        public void UpdateUserEmail(int id, string newEmail)
        {
            _service.UpdateUserEmail(id, newEmail);
            Console.WriteLine("User email updated successfully.");
        }

        public void PromoteUserToAdmin(int id)
        {
            _service.PromoteUserToAdmin(id);
            Console.WriteLine("User promoted to Admin role.");
        }
    }
}