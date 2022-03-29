import React from "react";
import { Rating } from "./Rating";
import { Card } from "react-bootstrap";
import { Link } from "react-router-dom";

const Product = ({ product }) => {
  return (
    <>
      <Card className="my-3 p-3 rounded">
        <Link to={`/products/${product.id}`}>
          <Card.Img src={product.image} />
        </Link>
        <Card.Body>
          <Link to={`/products/${product.id}`}>
            <Card.Title as="div">
              <strong>{product.title}</strong>
            </Card.Title>
          </Link>
          <Card.Text as="div" className="my-3">
            <Rating value={3} text={`${50} Reviews`} color={"#f8e825"}></Rating>
          </Card.Text>
          <Card.Text as="h3">{product.price}</Card.Text>
        </Card.Body>
      </Card>
    </>
  );
};
export default Product;
