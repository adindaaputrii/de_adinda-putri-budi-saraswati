-- buat database
create database alta_online_shop;

-- pakai database
use alta_online_shop;

-- buat tabel user
create table user(
	user_id int primary key auto_increment,
    nama varchar(100) not null,
    alamat varchar(100) not null,
    tanggal_lahir date not null,
    status_user enum ('Member', 'Bukan Member') not null,
    gender enum ('L', 'P') not null,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
);

-- buat tabel tipe produk
create table product_type(
	product_type_id int primary key auto_increment,
    product_type_name varchar(100) not null
);

-- buat tabel operator
create table operators(
	operator_id int primary key auto_increment,
    nama_operator varchar(100) not null
);

-- buat tabel desc produk
create table product_description(
	product_description_id int primary key auto_increment,
    description text not null
);

-- buat tabel payment method
create table payment_method(
	payment_method_id int primary key auto_increment,
    payment_method_name varchar(100) not null
);

-- buat tabel produk
create table product(
	product_id int primary key auto_increment,
    nama_product varchar(100) not null,
    product_type_id int not null,
    operator_id int not null,
    description_id int not null,
    payment_method_id int not null,
    foreign key (product_type_id) references product_type (product_type_id),
    foreign key (operator_id) references operators (operator_id),
    foreign key (description_id) references product_description (product_description_id),
    foreign key (payment_method_id) references payment_method (payment_method_id)
);

-- buat tabel transaksi
create table transaction(
	transaciton_id int primary key auto_increment,
    user_id int,
    total_amount double,
    transaction_date timestamp default current_timestamp,
    foreign key (user_id) references user (user_id)
);

-- buat tabel transaction detail
create table transaction_detail(
	transaction_detail_id int primary key auto_increment,
	transaction_id int,
    product_id int,
    quantity int,
    price double,
    foreign key (transaction_id) references transaction (transaciton_id),
    foreign key (product_id) references product (product_id)
);

-- buat tabel kurir
create table kurir(
	kurir_id int primary key auto_increment,
    kurir_name varchar(100) not null,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
);

-- tambah kolom ongkos_dasar di tabel kurir
alter table kurir add ongkos_dasar double;

-- rename tabel kurir menjadi tabel shipping
alter table kurir rename to shipping;

-- hapus tabel shipping
drop table shipping;

-- menambahkan entity baru dengan relation 1-to-1, 1-to-many, many-to-many
-- 1 to 1 dengan payment method
create table payment_method_description(
	payment_method_description int primary key auto_increment,
    payment_method_id int,
    payment_status varchar (100),
    foreign key (payment_method_id) references payment_method (payment_method_id)
);

-- 1 to many dengan user
create table address(
	address_id int primary key auto_increment,
    user_id int,
    jalan varchar(100) not null,
    kota varchar(100) not null,
    kode_pos int not null,
    foreign key (user_id) references user (user_id)
);

-- many to many user dengan payment method
create table user_payment_method_detail(
	user_id int,
    payment_method_id int,
    primary key (user_id, payment_method_id),
    foreign key (user_id) references user (user_id),
    foreign key (payment_method_id) references payment_method (payment_method_id)
);