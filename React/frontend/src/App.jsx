import { useState } from "react";
import Card from "./components/Card";

export default function App() {
  
  const fname = "Panchito"

  const data = [
    { id: 1, name: "Duck 🦆", brand: "Ducky", code: "FE342", price: 1200 },
    { id: 2, name: "Ball ⚽", brand: "FIFA", code: "RDE323", price: 345 },
    { id: 3, name: "Dino 🦕", brand: "Mattel", code: "DYE623", price: 300},
    { id: 4, name: "Racket 🎾", brand: "Wilson", code: "DUIW72", price: 3000 },
    { id: 5, name: "Car 🚗", brand: "HOTW HEELS", code: "DESW32", price: 23 },
  ];

  const [budget, setBudget] = useState(2000)

  return (
    <div className="bg-purple-800 text-white min-h-screen p-4 flex flex-col items-center">

      <div className="mb-4 space-y-5">

        <h1 className="text-3xl font-thin border-b-white border-b-0 m-3">
          Panchito World 🐶!
        </h1>

        <h2>Your budget is {budget}</h2>

        <label htmlFor="budget">Budget : </label>

        <input
          type="number"
          className="text-black"
          step={1000} id="budget"
          value={budget}
          onChange={(e) => setBudget(e.target.value)}
        />

      </div>

      <div className="grid grid-cols-3 gap-4">
        {data.map((el) => {
          return (
          <Card car={el} key={el.id} />
          );
        })}
      </div>

    </div>
  );
}
