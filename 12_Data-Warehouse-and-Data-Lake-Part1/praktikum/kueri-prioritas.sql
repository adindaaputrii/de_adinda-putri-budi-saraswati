-- PRIORITAS 1
-- buat tabel
create table users(
    id serial primary key, 
    username varchar not null, 
    password varchar not null, 
    created_at timestamp default current_timestamp, 
    updated_at timestamp default current_timestamp
) using columnar;

create table categories(
    id serial primary key, 
    name varchar not null, 
    created_at timestamp default current_timestamp, 
    updated_at timestamp default current_timestamp
) using columnar;

create table posts(
    id serial primary key, 
    user_id int, 
    category_id int, 
    title varchar not null, 
    content text, 
    created_at timestamp default current_timestamp, 
    update_at timestamp default current_timestamp
) using columnar;

create table comments(
    id serial primary key, 
    post_id int, 
    user_id int, 
    content varchar, 
    created_at timestamp default current_timestamp, 
    updated_at timestamp default current_timestamp
) using columnar;


-- menambahkan value ke tabel
insert into users(username, password) values ('nana', 'pass1');

insert into categories(name) values('reels');

insert into posts(user_id, category_id, title, content) values (1, 1, 'Travelling', 'Konten travelling ke Banyuwangi');

insert into comments(post_id, user_id, content) values (1, 1, 'Keren');



-- PRIORITAS 2
-- buat tabel
create table penyewa(
    id serial primary key, 
    nama varchar not null, 
    alamat varchar not null, 
    no_telp varchar not null
);

create table kendaraan(
    id serial primary key, 
    nopol varchar not null, 
    jenis_kendaraan varchar not null, 
    transmisi varchar not null
);

create table peminjaman(
    id serial primary key, 
    tgl_pinjam date default current_date, 
    tgl_kembali date default current_date, 
    id_penyewa int, 
    id_kendaraan int
);

create table pembayaran(
    id serial primary key, 
    jumlah_bayar float not null,
    tgl_bayar date default current_date, 
    id_peminjaman int
);

create table laporan_profit(
    id serial primary key, 
    keuntungan float not null, 
    bulan_laporan date default current_date, 
    id_peminjaman int
);

create table feedback(
    id serial primary key, 
    feedback_penyewa text not null, 
    rating int not null, 
    id_penyewa int, 
    id_peminjaman int
);

-- menambahkan value ke tabel
insert into penyewa (nama, alamat, no_telp) 
select 
    'penyewa' || d, 
    'alamat' || d || ', Jakarta', 
    '0812345678' || d 
from generate_series(1, 100) d;

insert into kendaraan (nopol, jenis_kendaraan, transmisi)
select 
    'B ' || d || ' ABC',
    CASE WHEN d % 2 = 0 THEN 'Mobil' ELSE 'Motor' END,
    CASE WHEN d % 3 = 0 THEN 'Manual' ELSE 'Matic' END
from generate_series(1, 100) d;


-- execute citus
docker exec -it citus psql -U postgres

-- sharding
select create_distributed_table('penyewa', 'id');
select * from citus_shards;

-- replication
set citus.shard_replication_factor = 2;
select * from pg_dist_placement;