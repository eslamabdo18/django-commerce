import axios from "axios";
import { Container, Row, Col } from "react-bootstrap";

import React, { useState, useEffect } from "react";
import Product from "../components/Product";

const HomeScreen = () => {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    // const { data } = await commerce.products.list();
    const url = "http://localhost:8000/store/products";
    axios.get(url).then((response) => {
      setProducts(response.data);
    });

    console.log(products);
    // setProducts(data);
  };

  useEffect(() => {
    console.log("hi");
    fetchProducts();
  }, []);

  return (
    <>
      <h1>Latest Products</h1>
      <Row>
        {products.map((product) => (
          <Col key={product.id} sm={12} md={6} lg={4} xl={3}>
            <Product product={product} />
          </Col>
        ))}
      </Row>
    </>
  );
};

export default HomeScreen;
