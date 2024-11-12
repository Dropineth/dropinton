# dropinton
TON | Hackers League: Winter 2024


# Pitch video


# Demo link



**README** that combines the Gate and TON wallet integration with the tree planting fund, and introduces a stable arbitrage mechanism for TON and USDT.

---

# Dropin Project: Decentralized Lottery with Tree Planting Fund

## Overview

Dropin is a decentralized application (DApp) leveraging blockchain technology, designed to engage users in sustainable practices through gamified lotteries and environmental impact. Dropin allows users to participate in a lottery system, where funds are allocated to real-world reforestation initiatives, like the UN’s Great Green Wall and AFR100, through the sale of NFTs that represent various environmental assets.

### Key Features

- **TON Wallet Integration**: Users can connect their TON wallets to participate in the lottery.
- **Gate Wallet Integration**: Enables cross-platform support with Gate Wallet for ease of transaction and token management.
- **Tree Planting Fund**: A portion of the lottery pool is allocated to a fund that supports reforestation efforts through NFT rewards.
- **Stable Arbitrage**: TON-USDT swap mechanism ensures that the value of the Tree Planting Fund remains stable and appreciates over time.

---

## Components

### 1. **User Wallet Integration**

- **TON Wallet**: Allows users to deposit and withdraw TON tokens to participate in the lottery.
- **Gate Wallet**: Integrated for broader ecosystem compatibility, enabling seamless interactions with Dropin's services.

### 2. **Lucky Draw Mechanism**

- **Prize Distribution**:
  - **70% of the prize pool** is allocated to a grand winner ("锦鲤"), who receives 70 TON.
  - **20% of the prize pool** is distributed to 99 participants as NFT rewards (Solar Power Station, Air Water Station, Drip Irrigation Network, Tree Seedlings, Grass Seeds).
  - **10% of the prize pool** is allocated to the Dropin team for operational costs, including 1% for each user that invites a new participant.

### 3. **Tree Planting Fund**

- **NFT Rewards**:
  - **Solar Power Station**
  - **Air Water Station**
  - **Drip Irrigation Network**
  - **Tree Seedlings (Native to Africa, high carbon sequestration)**
  - **Grass Seeds (Native to Africa, high carbon sequestration)**

- **Fund Management**:
  - Fund size and distribution will be tracked in both **TON** and **USDT**.
  - **TON to USDT Conversion**: When the price of TON peaks, a swap occurs, converting TON into USDT and storing it in the Tree Planting Fund, ensuring the fund’s value appreciates and maintains stability.

---

## How it Works

### Lottery Process

1. **User Participation**: Users connect their TON or GATE wallets and pay 1 TON to enter the lottery.
2. **Prize Pool Allocation**: 
   - 70% of the pool goes to the grand winner.
   - 20% is distributed as NFT rewards to 99 random participants.
   - 10% is kept for Dropin’s operations.
3. **NFT Distribution**: After the lottery draw, the NFTs representing environmental assets are randomly distributed.
4. **Tree Planting Progress**: A progress bar shows the current completion of the tree planting goal in hectares, indicating the overall progress of the Great Green Wall initiative.

---

## **Stable Arbitrage Mechanism**

The **Stable Arbitrage Mechanism** ensures the Tree Planting Fund’s value remains stable by monitoring the TON price and triggering automatic swaps to USDT when TON’s price reaches a peak. This ensures that the fund is protected from market volatility and continues to grow consistently, supporting reforestation projects without the risk of devaluation.

### **How it Works:**

1. **TON Price Monitoring**: The system constantly monitors the TON market price.
2. **Swap Trigger**: Once TON’s price exceeds a predefined threshold, the system automatically swaps TON for USDT at a 1:1 ratio.
3. **Fund Growth**: The swapped USDT is added to the Tree Planting Fund, ensuring the fund grows and remains stable.### Stable Arbitrage Mechanism

### **TON-USDT Swap:**

The **Stable Arbitrage Mechanism** aims to protect the Tree Planting Fund from the volatility of the TON token. When the value of TON spikes, the system automatically triggers a swap to USDT at a 1:1 ratio. This helps maintain the fund’s stability and protects it from the potential devaluation caused by market fluctuations in TON’s value.

To implement this, the following steps are followed:

1. **Identify Optimal TON Price Point**: The mechanism constantly monitors the price of TON in the market. Once the price exceeds a predefined threshold, the system triggers the swap to USDT.

2. **Perform the Swap Using DeDust**: The swap is carried out via the **DeDust Protocol** using the Vault and Pool mechanisms. The Vault will receive the TON tokens and the Pool will handle the conversion to USDT.

3. **Track Fund Balance and Growth**: After the swap, the USDT is held in the Tree Planting Fund, ensuring its value is stable and continually growing. The fund’s growth is tracked via **LP tokens** and liquidity pool management.

---

### **Code Implementation for TON-USDT Swap (DeDust Protocol)**

Below is the implementation code using the **DeDust SDK** for the TON-USDT swap and the tracking of the Tree Planting Fund balance.

#### **1. Finding the Vault and Pool for TON-USDT Swap**

The following code demonstrates how to use **DeDust** to interact with the Vault and perform the swap once the price of TON reaches a peak:

```typescript
import { Asset, PoolType, Factory, VaultNative } from '@dedust/sdk';
import { Address, TonClient4 } from '@ton/ton';
import { toNano } from '@ton/core';

// Initialize TON client and Factory contract
const tonClient = new TonClient4({ endpoint: "https://mainnet-v4.tonhubapi.com" });
const factory = tonClient.open(Factory.createFromAddress(MAINNET_FACTORY_ADDR));

// Define TON and USDT as assets
const TON = Asset.native();
const USDT = Asset.jetton(Address.parse('YOUR_USDT_JETTON_ADDRESS'));

// Fetch Vault (TON) and Pool (TON, USDT)
const tonVault = tonClient.open(await factory.getNativeVault());
const pool = tonClient.open(await factory.getPool(PoolType.VOLATILE, [TON, USDT]));

// Ensure that the Vault and Pool are deployed
if ((await pool.getReadinessStatus()) !== ReadinessStatus.READY) {
  throw new Error('Pool (TON, USDT) does not exist.');
}

if ((await tonVault.getReadinessStatus()) !== ReadinessStatus.READY) {
  throw new Error('Vault (TON) does not exist.');
}
```

#### **2. Monitoring the TON Price and Triggering the Swap**

This section is responsible for monitoring TON’s price and executing the swap when it reaches a threshold:

```typescript
// Assume we have a function `getTONPrice()` that fetches the current TON price.
async function monitorAndSwap() {
  const tonPrice = await getTONPrice(); // Fetch TON price from an oracle or price feed.
  const swapThreshold = 1.5; // Define the TON price threshold for triggering the swap.

  if (tonPrice >= swapThreshold) {
    const amountIn = toNano('100'); // Example: Swap 100 TON to USDT.

    // Send the swap request to the Vault (TON)
    await tonVault.sendSwap(sender, {
      poolAddress: pool.address,
      amount: amountIn,
      gasAmount: toNano("0.25"),
    });

    console.log("TON to USDT swap completed successfully.");
  } else {
    console.log("TON price not high enough to trigger the swap.");
  }
}
```

#### **3. Tracking Fund Growth:**

The Tree Planting Fund balance in USDT is tracked using **Liquidity Pool** (LP) tokens issued to the fund address after each successful swap. The following code demonstrates how you can track this balance:

```typescript
const lpWallet = tonClient.open(await pool.getWallet(fundAddress)); // Fund’s wallet to track LP token balance
const fundBalance = await lpWallet.getBalance();

console.log(`Tree Planting Fund Balance in LP Tokens: ${fundBalance}`);
```

#### **Tracking the Swap Operation**

For each TON-to-USDT swap, you will need to log the transaction details to monitor fund growth and ensure proper execution. This can be done using the following code:

```typescript
// Log the swap transaction for audit and tracking
async function logSwapTransaction(senderAddress: string, amountIn: bigint) {
  const transactionId = await logTransaction(senderAddress, amountIn); // Implement logging function
  console.log(`Transaction recorded. ID: ${transactionId}`);
}
```

This log function can send transaction details to an off-chain service (e.g., database or analytics platform) for tracking fund flow and stability.

---


## Technical Overview

### **Smart Contracts**

The following smart contracts are responsible for the lottery process, NFT distribution, and the TON-USDT conversion mechanism.

```solidity
// Example of smart contract for swap logic
contract StableArbitrage {
    address public admin;
    uint public tonBalance;
    uint public usdtBalance;
    
    constructor() {
        admin = msg.sender;
    }
    
    function swapTONForUSDT(uint amount) public {
        require(msg.sender == admin, "Only admin can swap");
        require(amount <= tonBalance, "Insufficient TON balance");
        
        uint usdtAmount = amount * getTONToUSDTPrice();
        usdtBalance += usdtAmount;
        tonBalance -= amount;
        
        // Transfer USDT to Tree Fund
        transferToTreeFund(usdtAmount);
    }

    function getTONToUSDTPrice() private view returns (uint) {
        // Implement price fetch from oracle
        return 1; // Simplified for illustration
    }
    
    function transferToTreeFund(uint amount) private {
        // Logic to transfer funds to the tree planting fund
    }
}
```
---

## DeDust Protocol Integration (Future DeFi Expansion)

### 1. **DeFi Yield Maximizers**

Using the **DeDust Protocol**, users can deposit their TON or USDT in yield farming contracts to maximize their returns. Users can participate in liquidity pools and receive rewards in $TON or other tokens, helping increase the sustainability of the Tree Planting Fund.

### 2. **DeDust Swap Implementation**

Users can swap between TON and USDT directly on the DeDust protocol, utilizing automated market makers (AMMs) for efficient and low-cost trading.

### 3. **User-Facing DeFi Apps**

Create easy-to-use interfaces for users to interact with yield farming, staking, and swap features, helping grow the Dropin ecosystem and maximize environmental funding.

---

## Installation（building）

To run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Dropineth/dropinton/DropinProject/Dropin.git
   cd Dropin
   ```

2. Install dependencies (for smart contracts, etc.):
   ```bash
   npm install
   ```

3. Start the frontend (React or any other framework you're using):
   ```bash
   npm start
   ```

---

## Contributing

We welcome contributions! Please feel free to open an issue or submit a pull request. Make sure to follow the contribution guidelines and maintain consistency with the project's goals of sustainability and decentralization.

---

## Contact
For support or inquiries, contact us at dropineth@gmail.com

---
