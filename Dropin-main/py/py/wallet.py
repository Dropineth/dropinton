__date__ = '2024-10-14'


from py.base import BaseHandler, authenticated


class WalletSaveHandler(BaseHandler):
    """/api/wallet/save

    保存，更新钱包
    """
    @authenticated
    async def post(self):
        """update/save
        {
        "account": {
            "address": "0:7e6d621ab0f5dd26e6c697254c4c0e9e2f9161e8892f5c1840502bec5ca300c2",
            "chain": "-239",
            "walletStateInit": "te6cckECFgEARtUfKx8t+O0ZYkzQGSDeAA=",
            "publicKey": "2ffde4fc62ec4f04dd9e61eaec4f8fd469e89c05811b547cac7cb7e3b4658933"
            }
        }
        """
        user, body = self.current_user, self.json
        uid, address = user['uid'], body['account']['address']
        wallet_user = await self.db.fetchone('''
            SELECT * FROM users WHERE `wallet`=%s;
        ''', [address, ])
        if wallet_user is None:
            await self.db.execute('''
                UPDATE users SET wallet=%s WHERE uid=%s;
                INSERT INTO user_wallets (uid, `address`, account, create_time)
                    VALUES (%s, %s, %s, NOW())
            ''', [
                address, uid,
                uid, address, body,
            ])
        elif wallet_user['uid'] != uid:
            await self.db.execute('''
                UPDATE users SET wallet=NULL WHERE uid=%s;
                UPDATE users SET wallet=%s WHERE uid=%s;
                INSERT INTO user_wallets (uid, `address`, account, create_time)
                    VALUES (%s, %s, %s, NOW())
            ''', [
                wallet_user['uid'],
                address, uid,
                uid, address, body,
            ])
        # item = await self.db.fetchone('''
        #     SELECT * FROM user_wallets WHERE `address`=%s;
        # ''', [body['address'], ])
        # if item is None:
        #     await self.db.execute('''
        #         INSERT INTO user_wallets (uid, `address`, account, create_time)
        #             VALUES (%s, %s, %s, NOW())
        #     ''', [uid, body['address'], body, ])
        # elif item['uid'] != uid:
        #     await self.db.execute('''
        #         UPDATE user_wallets SET `uid`=%s, account=%s, update_time=NOW()
        #         WHERE address = %s;
        #     ''', [uid, body, body['address'], ])
        return self.success(message='save wallet success')
