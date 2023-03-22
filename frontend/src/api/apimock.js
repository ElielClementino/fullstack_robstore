import axios from 'axios'

export default {
    getWalletInfo: (user_id) => {
        return new Promise((resolve, reject) => {
          axios
            .get(`http://localhost:3004/wallet-info?user_id=${user_id}`)
            .then((response) => {
              return resolve(response.data[0])
            })
            .catch((error) => {
              return reject(error)
            })
        })
      },
    depositWalletMoney: (user_id, amount) => {
        return new Promise((resolve, reject) => {
            axios
            .get(`http://localhost:3004/wallet-info?user_id=${user_id}`).then((response) =>{
                const wallet = response.data[0]
                axios
                .put(`http://localhost:3004/wallet-info/${wallet.id}`, {
                    id: wallet.id,
                    user_id: user_id,
                    amount_stored: amount + wallet.amount_stored
                })
                .then((response) => {
                    return resolve(response.data)
                })
                .catch((error) => {
                  return reject(error)
                })
            })
        })
      },
      whoami: () => {
        return new Promise((resolve, reject) => {
          axios
            .get("http://localhost:3004/whoami")
            .then((response) => {
              return resolve(response.data)
            })
            .catch((error) => {
              return reject(error)
            })
        })
      },
}