import { Container } from "react-bootstrap";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import HomeScreen from "./pages/HomeScreen";
import { ProductScreen } from "./pages/ProductScreen";

function App() {
  return (
    <Router>
      <Header />
      <main>
        <Container>
          {/* <HomeScreen /> */}
          <Routes>
            <Route path="/" element={<HomeScreen />} exact />
            <Route path="/products/:id" element={<ProductScreen />} exact />
          </Routes>
        </Container>
      </main>
      <Footer />
    </Router>
  );
}

export default App;
