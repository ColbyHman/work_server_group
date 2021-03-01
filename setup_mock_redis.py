from redis import Redis

def main():
    redis = Redis()
    jobs = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    redis.hset("jobs_waiting", mapping=jobs)

if __name__ == "__main__":
    main()
