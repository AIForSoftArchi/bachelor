using Application.Services;
using System.Collections.Generic;

namespace Infrastructure.Data
{
    public class CustomerRepository
    {
        private readonly List<string> _data = new();

        public void Add(string name)
        {
            _data.Add(name);
        }

        public List<string> GetAll()
        {
            return _data;
        }
    }
}
