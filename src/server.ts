import express, {Request, Response} from 'express';
import getClient from './client/elasticsearch';
const app = express();
app.get('/', async (request: Request, response: Response) => {
    const client = getClient();

    //Criar um registro no elasticsearch
    const result = await client.index({
        index: 'elastic_teste', //definindo nome do index
        type:  'type_elastic_teste', //definindo tipo
        body: {
            user: 'USER',
            password: 'SENHA',
            email: 'EMAIL'
        }
    });

    //Fazer busca
    return response.json(result);
})
app.listen(3333, () => console.log('Running'));
