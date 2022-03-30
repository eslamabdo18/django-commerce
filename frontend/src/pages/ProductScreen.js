import { Link, useParams } from "react-router-dom";
import axios from "axios";
import React, { useState, useEffect } from "react";
import { Row, Col, Image, ListGroup, Button, Card } from "react-bootstrap";
import { Rating } from "../components/Rating";

export const ProductScreen = () => {
  const [product, setProduct] = useState([]);
  const { id } = useParams();

  const fetchProducts = async () => {
    // const { data } = await commerce.products.list();
    console.log(id);
    let url = `http://localhost:8000/store/products/${id}/`;
    let headers = { "Content-Type": "application/json" };
    axios.get(url, headers).then((response) => {
      setProduct(response.data);
    });

    console.log(product);
    // setProducts(data);
  };

  useEffect(() => {
    console.log("hi");
    fetchProducts();
    console.log(product);
    console.log("hi");
  }, []);

  return (
    <div>
      <Link to="/" className="btn btn-light my-3">
        Go Back
      </Link>
      <Row>
        <Col md={6}>
          <Image src={product.image} alt={product.title} fluid />
        </Col>
        <Col md={3}>
          <ListGroup variant="flush">
            <ListGroup.Item>
              <h3>{product.title}</h3>
            </ListGroup.Item>
            <ListGroup.Item>
              <Rating value={3} text={`${40} reviews`} color={"#f8e825"} />
            </ListGroup.Item>
            <ListGroup.Item>Price: $ {product.price}</ListGroup.Item>
            <ListGroup.Item>Description: {product.description}</ListGroup.Item>
          </ListGroup>
        </Col>
        <Col md={3}>
          <Card>
            <ListGroup variant="flush">
              <ListGroup.Item>
                <Row>
                  <Col>Price: </Col>
                  <Col>
                    <strong>$ {product.price}</strong>
                  </Col>
                </Row>
              </ListGroup.Item>

              <ListGroup.Item>
                <Row>
                  <Col>status: </Col>
                  <Col>
                    <strong>In stock</strong>
                  </Col>
                </Row>
              </ListGroup.Item>

              <ListGroup.Item>
                <Button className="btn-block" type="buttonn">
                  Add To Cart
                </Button>
              </ListGroup.Item>
            </ListGroup>
          </Card>
        </Col>
      </Row>
    </div>
  );
};
