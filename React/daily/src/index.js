import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";

const data = [
  {
    name: "Het",
    img: "https://picsum.photos/300/200?random=1",
    url: "https://www.linkedin.com/in/het-bhalani-20403b2a8/",
    about: "Machine learning Engineer at ABC Corp."
  },
  {
    name: "Dhruv",
    img: "https://picsum.photos/300/200?random=2",
    url:"https://www.linkedin.com/in/dhruv-chotai-179a502aa/",
    about: "Data Scientist at XYZ Ltd."
  },
  {
    name: "Meet",
    img: "https://picsum.photos/300/200?random=3",
    url:"https://linkedin.com/in/meet-padhiar-03344a2b4/",
    about: "Web Developer specializing in React."
  },
  {
    name: "Mann",
    img: "https://picsum.photos/300/200?random=4",
    url:"https://www.linkedin.com/in/mann-padhiar-9139972b3/",
    about: "Full Stack Developer at Tech Solutions."
  },
  {
    name: "Vandan",
    img: "https://picsum.photos/300/200?random=5",
    url:"https://www.linkedin.com/in/vandan-kholia-a63b82294/",
    about: "Mobile App Developer at Innovate Inc."
  },
];

const newarr = data.map((dude) => {
  return (
    
      <div className="col col-4">
        <div className="card my-3">
          <img src={dude.img} className="card-img-top" alt={dude.name} />
          <div className="card-body">
            <h5 className="card-title">{dude.name}</h5>
            <p className="card-text">
              {dude.about}
            </p>
            <button className="btn btn-primary"  onClick = {()=>window.open(dude.url, "_blank")}>
             
              LinkedIn
            </button>
          </div>
        </div>
      </div>
  );
});

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<>
  <div className="container-sm m-4">
    <div className="row">{newarr}</div>
  </div>
</>
);
