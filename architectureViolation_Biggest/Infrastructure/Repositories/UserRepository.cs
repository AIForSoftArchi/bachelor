using Core.Entities;

namespace Infrastructure.Repositories
{
    public class UserRepository
    {
        private readonly List<User> _users = new List<User>();

        public void AddUser(User user)
        {
            if (_users.Any(u => u.Email == user.Email))
                throw new Exception("User with this email already exists.");
            _users.Add(user);
        }

        public List<User> GetAllUsers() => _users;

        public User GetUserById(int id) => _users.FirstOrDefault(u => u.Id == id);

        public void RemoveUser(User user)
        {
            _users.Remove(user);
        }

        public void UpdateUser(User updatedUser)
        {
            var index = _users.FindIndex(u => u.Id == updatedUser.Id);
            if (index >= 0)
                _users[index] = updatedUser;
        }

        public List<User> FindUsersByRole(string role)
        {
            return _users.Where(u => u.Role.Equals(role, StringComparison.OrdinalIgnoreCase)).ToList();
        }

        public int CountActiveUsers()
        {
            return _users.Count(u => u.IsActive);
        }
    }
}