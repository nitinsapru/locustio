using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace LocustApplication.Controllers
{
    public class apiController : Controller
    {
        // GET: api
        public string RestEndpoint1()
        {
            return "Nitin Sapru";
        }

        public int RestEndpoint2()
        {
            return 123214;
        }
    }
}