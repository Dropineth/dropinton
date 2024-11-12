# dropinton
TON | Hackers League: Winter 2024
Here’s an updated **README** that combines the Gate and TON wallet integration with the tree planting fund, and introduces a stable arbitrage mechanism for TON and USDT.

---

# Dropin Project: Decentralized Lottery with Tree Planting Fund

## Overview

Dropin is a decentralized application (DApp) leveraging blockchain technology, designed to engage users in sustainable practices through gamified lotteries and environmental impact. Dropin allows users to participate in a lottery system, where funds are allocated to real-world reforestation initiatives, like the UN’s Great Green Wall, through the sale of NFTs that represent various environmental assets.

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

1. **User Participation**: Users connect their TON wallets and pay 1 TON to enter the lottery.
2. **Prize Pool Allocation**: 
   - 70% of the pool goes to the grand winner.
   - 20% is distributed as NFT rewards to 99 random participants.
   - 10% is kept for Dropin’s operations.
3. **NFT Distribution**: After the lottery draw, the NFTs representing environmental assets are randomly distributed.
4. **Tree Planting Progress**: A progress bar shows the current completion of the tree planting goal in hectares, indicating the overall progress of the Great Green Wall initiative.

### Stable Arbitrage Mechanism

1. **TON-USDT Swap**: When TON’s value reaches a peak, it will be swapped for USDT at a 1:1 ratio to stabilize the Tree Planting Fund.
2. **Fund Growth**: The Tree Planting Fund is continually growing and will provide consistent support for reforestation projects, without risk of devaluation due to TON market fluctuations.

---

## Technical Overview

### 1. **Smart Contracts**

The following smart contracts are responsible for the lottery process, NFT distribution, and the TON-USDT conversion mechanism.

```solidity
// Lottery smart contract (Solidity)
contract DropinLottery {
    address public admin;
    uint public totalPool;
    mapping(address => uint) public participantBalances;
    address[] public participants;
    
    constructor() {
        admin = msg.sender;
    }
    
    function participate() public payable {
        require(msg.value == 1 ether, "Must send 1 TON to participate");
        totalPool += msg.value;
        participants.push(msg.sender);
    }
    
    function drawLottery() public {
        require(msg.sender == admin, "Only admin can draw");
        
        uint winnerIndex = random() % participants.length;
        address winner = participants[winnerIndex];
        
        // Distribute the rewards
        payable(winner).transfer(totalPool * 70 / 100);
        distributeNFTs(participants);
        
        // Reset the lottery
        totalPool = 0;
        delete participants;
    }

    function distributeNFTs(address[] memory participants) private {
        // Logic to randomly distribute NFTs to 99 participants
    }
    
    function random() private view returns (uint) {
        return uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, participants)));
    }
}
```

### 2. **TON-USDT Swap Mechanism**

This contract will manage the swap between TON and USDT, based on market conditions:

```solidity
// TON-USDT Swap Smart Contract (Solidity)
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
        
        // Example swap logic: Swap TON for USDT at the current rate
        uint usdtAmount = amount * getTONToUSDTPrice();
        usdtBalance += usdtAmount;
        tonBalance -= amount;
        
        // Transfer USDT to Tree Fund
        transferToTreeFund(usdtAmount);
    }

    function getTONToUSDTPrice() private view returns (uint) {
        // Implement market price fetch logic (e.g., using Chainlink or other oracles)
        return 1;  // Simplified for illustration
    }
    
    function transferToTreeFund(uint amount) private {
        // Logic to transfer funds to the tree planting fund
    }
}
```

---

## DeDust Protocol Integration (Future DeFi Expansion)

### 1. **DeFi Yield Maximizers**

Using the **DeDust Protocol**, users can deposit their TON or USDT in yield farming contracts to maximize their returns. Users can participate in liquidity pools and receive rewards in $DROP or other tokens, helping increase the sustainability of the Tree Planting Fund.

### 2. **DeDust Swap Implementation**

Users can swap between TON, USDT, and $DROP directly on the DeDust protocol, utilizing automated market makers (AMMs) for efficient and low-cost trading.

### 3. **User-Facing DeFi Apps**

Create easy-to-use interfaces for users to interact with yield farming, staking, and swap features, helping grow the Dropin ecosystem and maximize environmental funding.

---

## Installation

To run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/DropinProject/Dropin.git
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

Feel free to expand or modify the details based on any additional specifications or features!
