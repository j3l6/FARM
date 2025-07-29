import React from 'react'

const Card = ({ car: { name, brand, code, price } }) => {
  return (
    <div className="bg-white rounded m-4 p-4 shadow-lg">
      <h1 className="test-2x1 text-gray-600">{name}</h1>
      <p className="text-sm text-gray-600">{brand} - {code}</p>
      <p className="test-lg text-right text-gray-600 align-text-bottom">${price}</p>
    </div>
  )
}
export default Card;
