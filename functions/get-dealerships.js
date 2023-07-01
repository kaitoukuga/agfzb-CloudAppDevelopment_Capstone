function main(params) {
    const { CloudantV1 } = require('@ibm-cloud/cloudant');
    const { IamAuthenticator } = require('ibm-cloud-sdk-core');
    const authenticator = new IamAuthenticator({ apikey: 'TSgWbTjzq6jssiS84dyhno1-8Ndsegw233QlFv51JGLw' });
    const cloudant = CloudantV1.newInstance({
      authenticator: authenticator,
    });
    cloudant.setServiceUrl('https://28059ad8-d624-49da-9bc2-b47b4fe4f5cf-bluemix.cloudantnosqldb.appdomain.cloud');
  
    return new Promise((resolve, reject) => {
      if (params.state) {
        findDealershipByState(cloudant, params.state)
          .then((result) => {
            const code = result.length ? 200 : 404;
            resolve({
              statusCode: code,
              headers: { 'Content-Type': 'application/json' },
              body: result,
            });
          })
          .catch((err) => {
            console.error(err);
            reject({
              statusCode: 500,
              headers: { 'Content-Type': 'application/json' },
              body: { error: 'Internal Server Error' },
            });
          });
      } else if (params.id) {
        findDealershipById(cloudant, params.id)
          .then((result) => {
            const code = result.length ? 200 : 404;
            resolve({
              statusCode: code,
              headers: { 'Content-Type': 'application/json' },
              body: result,
            });
          })
          .catch((err) => {
            console.error(err);
            reject({
              statusCode: 500,
              headers: { 'Content-Type': 'application/json' },
              body: { error: 'Internal Server Error' },
            });
          });
      } else {
        findAllDealerships(cloudant)
          .then((result) => {
            const code = result.length ? 200 : 404;
            resolve({
              statusCode: code,
              headers: { 'Content-Type': 'application/json' },
              body: result,
            });
          })
          .catch((err) => {
            console.error(err);
            reject({
              statusCode: 500,
              headers: { 'Content-Type': 'application/json' },
              body: { error: 'Internal Server Error' },
            });
          });
      }
    });
  }
  
  function findDealershipByState(cloudant, state) {
    return new Promise((resolve, reject) => {
      cloudant
        .postFind({ db: 'dealerships', selector: { state: state } })
        .then((result) => {
          resolve(result.result.docs);
        })
        .catch((err) => {
          reject(err);
        });
    });
  }
  
  function findDealershipById(cloudant, id) {
    return new Promise((resolve, reject) => {
      cloudant
        .postFind({ db: 'dealerships', selector: { id: parseInt(id) } })
        .then((result) => {
          resolve(result.result.docs);
        })
        .catch((err) => {
          reject(err);
        });
    });
  }
  
  function findAllDealerships(cloudant) {
    return new Promise((resolve, reject) => {
      cloudant
        .postAllDocs({ db: 'dealerships', includeDocs: true, limit: 10 })
        .then((result) => {
          resolve(result.result.rows);
        })
        .catch((err) => {
          reject(err);
        });
    });
  }