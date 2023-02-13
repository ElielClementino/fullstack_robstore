import api from "./config.js"

export default {
  addNewProduct: (product) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/products/add/product", {product})
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  listProducts: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/products/list/products")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  filterProducts: (products) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/products/filter/products", products)
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  buyProducts: (products) => {
    return new Promise((resolve, reject) => {
      api
        .patch("/api/products/buy/products", products)
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  }
}
