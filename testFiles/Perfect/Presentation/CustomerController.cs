namespace OnionArchitecture.Presentation
{
    using Microsoft.AspNetCore.Mvc;
    using OnionArchitecture.Application;

    [ApiController]
    [Route("api/customers")]
    public class CustomerController : ControllerBase
    {
        private readonly ICustomerService _customerService;
        
        public CustomerController(ICustomerService customerService)
        {
            _customerService = customerService;
        }

        [HttpGet("{id}")]
        public IActionResult GetCustomer(int id)
        {
            var customer = _customerService.GetCustomer(id);
            if (customer == null)
                return NotFound();
            return Ok(customer);
        }

        [HttpPost]
        public IActionResult CreateCustomer([FromBody] CreateCustomerRequest request)
        {
            _customerService.CreateCustomer(request.Name, request.Email);
            return CreatedAtAction(nameof(GetCustomer), new { id = request.Name }, request);
        }
    }

    public record CreateCustomerRequest(string Name, string Email);
}
