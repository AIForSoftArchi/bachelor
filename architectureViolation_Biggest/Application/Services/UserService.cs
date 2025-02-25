// Application/Services/UserService.cs
using Core.Entities;
using Infrastructure.Repositories;

namespace Application.Services
{
    public class UserService
    {
        private readonly UserRepository _repository;

        public UserService(UserRepository repository)
        {
            _repository = repository;
        }

        public void AddUser(User user)
        {
            if (!user.IsEmailValid())
                throw new Exception("Invalid email address.");

            if (!user.IsAdult())
                throw new Exception("User must be at least 18 years old.");

            _repository.AddUser(user);
        }

        public List<User> GetAllUsers() => _repository.GetAllUsers();

        public User GetUserById(int id)
        {
            var user = _repository.GetUserById(id);
            if (user == null)
                throw new Exception("User not found.");
            return user;
        }

        public void DeleteUser(int id)
        {
            var user = GetUserById(id);
            user.DeactivateUser();
            _repository.UpdateUser(user);
        }

        public void UpdateUserEmail(int id, string newEmail)
        {
            var user = GetUserById(id);
            if (!newEmail.Contains("@"))
                throw new Exception("Invalid email format.");
            user.Email = newEmail;
        }

        public void UpdateUserAddress(int id, string newAddress)
        {
            var user = GetUserById(id);
            user.UpdateAddress(newAddress);
        }

        public void PromoteUserToAdmin(int id)
        {
            var user = GetUserById(id);
            user.Role = "Admin";
        }

        public List<User> GetInactiveUsers()
        {
            return _repository.GetAllUsers().Where(u => !u.IsActive).ToList();
        }
    }
}