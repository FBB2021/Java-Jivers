let todo = [
	{
		name: "Apple",
		brand: "Wai Yee Electronic Limited",
		category: "Centurion Garden & Outdoor",
		location: 3709,
		quantity: 70,
		"Weight(kg)": 389.78,
		id: 1,
	},
	{
		name: "Grnpe air",
		brand: "Josephine Engineering Inc.",
		category: "Household & Kitchen Appliances",
		location: 7669,
		quantity: 188,
		id: 2,
		"weight(kg)": 455.26,
	},
	{
		name: "xKiwi",
		brand: "Anqi Industrial Company Limited",
		category: "Beauty & Personal Care",
		location: 6923,
		quantity: 102,
		id: 3,
		"Weight(kg)": 149.17,
	},
	{
		name: "xApple",
		brand: "Feng Kee Trading Company Limited",
		category: "Industrial & Scientific Supplies",
		location: 1252,
		quantity: 48,
		"weight(kg)": 193.57,
		id: 4,
	},
	{
		name: "kango core",
		brand: "Chi Yuen Development & Trading Limited",
		category: "Cell Phones & Accessories",
		location: 4684,
		quantity: 162,
		id: 5,
		"weight(kg)": 368.41,
	},
	{
		name: "Cgerry",
		brand: "Garza Telecommunication Inc.",
		category: "Tools & Home Decoration",
		location: 7305,
		quantity: 10,
		id: 6,
		"weight(kg)": 266.43,
	},
	{
		name: "omni-Grape",
		brand: "Itsuki Toy Corporation",
		category: "Handcrafts",
		location: 6741,
		quantity: 88,
		id: 7,
		"weight(kg)": 462.48,
	},
	{
		name: "Rxmbutan",
		brand: "Takeda Corporation",
		category: "Baby",
		location: 5015,
		quantity: 11,
		id: 8,
		"Weight(kg)": 92.5,
	},
	{
		name: "upple",
		brand: "Tao Industrial Company Limited",
		category: "Industrial & Scientific Supplies",
		location: 9863,
		quantity: 133,
		id: 9,
		"Weight(kg)": 424.68,
	},
	{
		email: "useremail",
		password: "userpassword",
		type: "general_user",
	},
	{
		email: "adminemail",
		password: "adminpassword",
		type: "admin_user",
	},
];

module.exports = function () {
	return {
		todo: todo,
	};
};
