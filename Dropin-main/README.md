# Dropin

DROPINTON

Web3Labs X TON Foundation Global Accelerator Program


Dropin Project: Decentralized Lottery with Tree Planting Fund

Overview

Dropin is a decentralized application (DApp) leveraging blockchain technology, designed to engage users in sustainable practices through gamified lotteries and environmental impact. Dropin allows users to participate in a lottery system, where funds are allocated to real-world reforestation initiatives, like the UN’s Great Green Wall and AFR100, through the sale of NFTs that represent various environmental assets.

Key Features

TON & Gate Wallet Integration:

Seamless wallet connectivity for deposits and withdrawals.
Cross-platform compatibility for broader user access.
Decentralized Lottery:

70% of the prize pool is awarded to a grand winner.
20% is distributed as NFTs representing environmental assets like solar power stations and tree seeds.
Tree Planting Fund:

Supports reforestation projects through the proceeds of NFTs.
Users also have a chance to receive $DOP tokens as random rewards from the fund.（building）
Stable Arbitrage:

A TON-USDT swap mechanism maintains the stability of the Tree Planting Fund by converting TON into USDT during price surges.
Referral Rewards:

Invite new users to participate in the lottery.
Top 3 referrers earn rewards: 5 TON, 2 TON, and 1 TON, respectively.
AdTON Advertising Module: （building）

Airdrops from partner projects are randomly distributed into the lottery prize pool to incentivize participation and collaboration.
Components

1. User Wallet Integration

TON Wallet: Allows users to deposit and withdraw TON tokens to participate in the lottery.
Gate Wallet: Integrated for broader ecosystem compatibility, enabling seamless interactions with Dropin's services.
2. Lucky Draw Mechanism

Prize Distribution:
70% of the prize pool is allocated to a grand winner ("锦鲤"), who receives 70 TON.
20% of the prize pool is distributed to 99 participants as NFT rewards (Solar Power Station, Air Water Station, Drip Irrigation Network, Tree Seedlings, Grass Seeds).
10% of the prize pool is allocated to the Dropin team for operational costs, including 1% for each user that invites a new participant.
3. Tree Planting Fund

NFT Rewards:

Solar Power Station
Air Water Station
Drip Irrigation Network
Tree Seedlings (Native to Africa, high carbon sequestration)
Grass Seeds (Native to Africa, high carbon sequestration)
Fund Management:

Fund size and distribution will be tracked in both TON and USDT.
TON to USDT Conversion: When the price of TON peaks, a swap occurs, converting TON into USDT and storing it in the Tree Planting Fund, ensuring the fund’s value appreciates and maintains stability.
How it Works

Lottery Process

User Participation: Users connect their TON or GATE wallets and pay 1 TON to enter the lottery.
Prize Pool Allocation:
70% of the pool goes to the grand winner.
20% is distributed as NFT rewards to 99 random participants.
10% is kept for Dropin’s operations.
NFT Distribution: After the lottery draw, the NFTs representing environmental assets are randomly distributed.
Tree Planting Progress: A progress bar shows the current completion of the tree planting goal in hectares, indicating the overall progress of the Great Green Wall initiative.
Referral Rewards:
Invite new users to participate in the lottery.
Top 3 referrers earn rewards: 5 TON, 2 TON, and 1 TON, respectively.
Step-by-Step Process Breakdown

1. User Participation:

Users connect their TON or Gate Wallet and pay 1 TON to enter the lottery.

TON Wallet Integration: Users should connect their wallets to the app, which can be done using the TON SDK for mini apps.
// Assuming we have TON SDK integrated in the mini app
const tonSdk = new TONSDK();  // TON SDK instance

// Function to connect the TON wallet
async function connectWallet() {
  try {
    const wallet = await tonSdk.wallet.connect();  // Connects the wallet
    console.log("Connected to wallet: ", wallet.address);
  } catch (error) {
    console.error("Error connecting wallet: ", error);
  }
}

// Example: User presses a button to connect their wallet
document.getElementById("connect-btn").addEventListener("click", connectWallet);
2. Prize Pool Allocation:

70% of the prize pool goes to the grand winner, 20% is distributed as NFT rewards to 99 random participants, and 10% is kept for Dropin's operations.

// Simulate the Prize Pool Allocation
const prizePool = 1000;  // Total pool amount in TON
const grandPrize = prizePool * 0.7;  // 70% to grand winner
const nftRewards = prizePool * 0.2;  // 20% to 99 participants
const operationalFund = prizePool * 0.1;  // 10% for Dropin operations

// Simulate winner and participant allocation
const grandWinner = "0x123abc";  // Example grand winner address
const nftParticipants = Array(99).fill().map(() => generateRandomAddress());  // Simulate 99 random participants

function generateRandomAddress() {
  return "0x" + Math.random().toString(16).slice(2, 18);
}

// Output the prize pool details
console.log("Grand Winner: ", grandWinner);
console.log("NFT Rewards: ", nftParticipants);
console.log("Operational Fund: ", operationalFund);
3. NFT Distribution:

After the lottery draw, NFTs representing environmental assets are randomly distributed to 99 participants.

// Simulating NFT distribution (e.g., tree seeds, solar panels, etc.)
function distributeNFTs() {
  const environmentalNFTs = ['Tree Seed NFT', 'Solar Power NFT', 'Water Station NFT', 'Drip Irrigation NFT'];
  const nftAllocations = nftParticipants.map(() => {
    const randomNFT = environmentalNFTs[Math.floor(Math.random() * environmentalNFTs.length)];
    return randomNFT;
  });

  console.log("NFT Distribution: ", nftAllocations);
}

// Call to distribute NFTs after the lottery draw
distributeNFTs();
4. Tree Planting Progress:

A progress bar tracks the tree planting goal, showing hectares planted.

// Simulating tree planting progress
let hectaresPlanted = 1000000;  // Total hectares planted globally
let currentProgress = 0.1;  // Progress percentage (10%)

// Update progress bar (for example, in a UI component)
function updateProgress() {
  const progressBar = document.getElementById("progress-bar");
  progressBar.style.width = `${currentProgress * 100}%`;  // Update progress bar
  console.log(`Current Progress: ${currentProgress * 100}%`);
}

// Call the progress update function periodically
setInterval(updateProgress, 1000);  // Update every 1 second for demo
5.Referral Rewards Distribution

// Simulate top 3 referrers and reward distribution
const referrers = [
  { name: "User A", invites: 50 },
  { name: "User B", invites: 30 },
  { name: "User C", invites: 20 },
];

const rewards = [5, 2, 1]; // Rewards in TON for top 3

referrers.slice(0, 3).forEach((referrer, index) => {
  console.log(`${referrer.name} receives ${rewards[index]} TON for ${referrer.invites} invites`);
});
Dropin Lucky Draw Mini App (TON Integration)

Overview

The Dropin Lucky Draw is a TON-based decentralized application (DApp) designed to gamify reforestation efforts and engage the community through blockchain technology. This app enables users to participate in a lottery that funds tree-planting projects and rewards participants with NFTs tied to environmental assets.

Features

TON Wallet Integration: Connect with Gate or TON wallet to participate in the lottery.
Lottery Prize Pool Allocation: 70% goes to the grand prize winner, 20% to 99 NFT recipients, and 10% for Dropin operations.
NFT Rewards: Random distribution of NFTs, including solar power stations, air water stations, and carbon-sequestering tree seeds.
Tree Planting Progress: A progress bar that tracks the overall planting goal of 1 billion hectares.
Referral Rewards:
Invite new users to participate in the lottery.
Top 3 referrers earn rewards: 5 TON, 2 TON, and 1 TON, respectively.
How It Works

1. User Participation:

Connect your TON or Gate wallet and pay 1 TON to enter the lottery.
2. Prize Pool Allocation:

70% of the pool is awarded to the grand winner.
20% is distributed as NFT rewards to 99 random participants.
10% is kept for Dropin's operational costs.
3. NFT Distribution:

After the lottery draw, NFTs representing environmental assets are randomly distributed to 99 participants.
4. Tree Planting Progress:

A progress bar shows the current completion of the tree planting goal, measured in hectares.
5.Referral Rewards:

Invite new users to participate in the lottery.
Top 3 referrers earn rewards: 5 TON, 2 TON, and 1 TON, respectively.
Code Example

Sample Code Snippet for Prize Pool Allocation (JavaScript)

// Simulate the Prize Pool allocation
const prizePool = 1000; // Total pool amount in TON
const grandPrize = prizePool * 0.7; // 70% goes to grand winner
const nftRewards = prizePool * 0.2; // 20% distributed to 99 random participants
const operationalFund = prizePool * 0.1; // 10% for Dropin operations

// Winner distribution
const grandWinner = "0x123abc"; // Example wallet address
const nftParticipants = Array(99).fill().map(() => generateRandomAddress()); // Simulate 99 random participants

console.log("Grand Winner: ", grandWinner);
console.log("NFT Rewards for 99 Participants: ", nftParticipants);
console.log("Operational Fund: ", operationalFund);

// Helper function to generate random addresses for participants (simulation)
function generateRandomAddress() {
  return "0x" + Math.random().toString(16).slice(2, 18);
}

// Simulating the result display
function displayResults() {
  alert(`Grand Prize: ${grandPrize} TON awarded to: ${grandWinner}`);
  alert(`NFT rewards (Total: ${nftRewards} TON) distributed to 99 participants`);
  alert(`Dropin Operational Fund: ${operationalFund} TON`);
}

// Call the display function to show results
displayResults();
Stable Arbitrage Mechanism

The Stable Arbitrage Mechanism ensures the Tree Planting Fund’s value remains stable by monitoring the TON price and triggering automatic swaps to USDT when TON’s price reaches a peak. This ensures that the fund is protected from market volatility and continues to grow consistently, supporting reforestation projects without the risk of devaluation.

How it Works:

TON Price Monitoring: The system constantly monitors the TON market price.
Swap Trigger: Once TON’s price exceeds a predefined threshold, the system automatically swaps TON for USDT at a 1:1 ratio.
Fund Growth: The swapped USDT is added to the Tree Planting Fund, ensuring the fund grows and remains stable.### Stable Arbitrage Mechanism
TON-USDT Swap:

The Stable Arbitrage Mechanism aims to protect the Tree Planting Fund from the volatility of the TON token. When the value of TON spikes, the system automatically triggers a swap to USDT at a 1:1 ratio. This helps maintain the fund’s stability and protects it from the potential devaluation caused by market fluctuations in TON’s value.

To implement this, the following steps are followed:

Identify Optimal TON Price Point: The mechanism constantly monitors the price of TON in the market. Once the price exceeds a predefined threshold, the system triggers the swap to USDT.

Perform the Swap Using DeDust: The swap is carried out via the DeDust Protocol using the Vault and Pool mechanisms. The Vault will receive the TON tokens and the Pool will handle the conversion to USDT.

Track Fund Balance and Growth: After the swap, the USDT is held in the Tree Planting Fund, ensuring its value is stable and continually growing. The fund’s growth is tracked via LP tokens and liquidity pool management.

Code Implementation for TON-USDT Swap (DeDust Protocol)

Below is the implementation code using the DeDust SDK for the TON-USDT swap and the tracking of the Tree Planting Fund balance.

1. Finding the Vault and Pool for TON-USDT Swap

The following code demonstrates how to use DeDust to interact with the Vault and perform the swap once the price of TON reaches a peak:

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
2. Monitoring the TON Price and Triggering the Swap

This section is responsible for monitoring TON’s price and executing the swap when it reaches a threshold:

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
3. Tracking Fund Growth:

The Tree Planting Fund balance in USDT is tracked using Liquidity Pool (LP) tokens issued to the fund address after each successful swap. The following code demonstrates how you can track this balance:

const lpWallet = tonClient.open(await pool.getWallet(fundAddress)); // Fund’s wallet to track LP token balance
const fundBalance = await lpWallet.getBalance();

console.log(`Tree Planting Fund Balance in LP Tokens: ${fundBalance}`);
Tracking the Swap Operation

For each TON-to-USDT swap, you will need to log the transaction details to monitor fund growth and ensure proper execution. This can be done using the following code:

// Log the swap transaction for audit and tracking
async function logSwapTransaction(senderAddress: string, amountIn: bigint) {
  const transactionId = await logTransaction(senderAddress, amountIn); // Implement logging function
  console.log(`Transaction recorded. ID: ${transactionId}`);
}
This log function can send transaction details to an off-chain service (e.g., database or analytics platform) for tracking fund flow and stability.

Technical Overview

Smart Contracts

The following smart contracts are responsible for the lottery process, NFT distribution, and the TON-USDT conversion mechanism.

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
DeDust Protocol Integration (Future DeFi Expansion)

1. DeFi Yield Maximizers

Using the DeDust Protocol, users can deposit their TON or USDT in yield farming contracts to maximize their returns. Users can participate in liquidity pools and receive rewards in $TON or other tokens, helping increase the sustainability of the Tree Planting Fund.

2. DeDust Swap Implementation

Users can swap between TON and USDT directly on the DeDust protocol, utilizing automated market makers (AMMs) for efficient and low-cost trading.

3. User-Facing DeFi Apps

Create easy-to-use interfaces for users to interact with yield farming, staking, and swap features, helping grow the Dropin ecosystem and maximize environmental funding.

Installation（building）

To run the project locally:

Clone the repository:

git clone https://github.com/Dropineth/dropinton/DropinProject/Dropin.git
cd Dropin
Install dependencies (for smart contracts, etc.):

npm install
Start the frontend (React or any other framework you're using):

npm start
Contributing

We welcome contributions! Please feel free to open an issue or submit a pull request. Make sure to follow the contribution guidelines and maintain consistency with the project's goals of sustainability and decentralization.

Contact

For support or inquiries, contact us at dropineth@gmail.com

TEAM

Y.C. Co-FOUNDER

A seasoned blockchain and full-stack development expert with over a decade of experience at top-tier companies like HashKey Cloud, Binance, and MyTV Super, leading innovative Web3 solutions, enhancing security architectures, driving DeFi product development, and optimizing system operations across diverse industries.

CAT BOSS Co-FOUNDER

With over 15 years of experience in internet technology, including roles at renowned companies such as McCann Worldgroup, Hopen, and ISAILSOFT, I bring expertise in global project collaboration, B2B2C technical solutions, and Web3 product development.

YU Co_FOUNDER

Host of Shenzhen HackathonWeekly, Initiator of AI Co-learning Sessions on Tuesday and Thursday evenings.
Five years of experience as a UX designer in top-tier tech companies. , specializing in consumer-facing content monetization products (serving both domestic and international markets) and high-engagement tools (with tens of millions of daily active users). Proficient in B2B AI backend design, with extensive expertise in end-to-end design and user experience optimization.

RUBY Co_FOUNDER

A full-stack developer with 10 years of experience in big data, e-commerce, and online education. Led large front-end teams, delivering projects like data monitoring and micro-frontend implementation. Over the past year, focused on Web3, contributing to multiple hackathons and gaining hands-on experience across various blockchains, driving practical blockchain applications.

LEE FOUNDER

10+ years of experience in TMT \Consumer\ ESG investment research. Focused on sustainable killer applications in Web2 and Web3. Former member of CMRC's science and technology enterprise marketing and business growth research group.
